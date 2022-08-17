def get_sample_stack(samples):
    """
    createSampleStack returns a dictionary of ROOT.THStacks, 
    which correspond to data, signal and background 
    
    Args:
        samples (Dict): Dictionary of all samples we with to plot 
    Return:
        stack (Dict (ROOT.THStack)): The stack dictionary for all sample types 
        and legend entries. 
    """
    import ROOT
    stack = {}
    for Type in ['data','bkg','fakes', 'sig']:
        stack[Type] = {}
        for sample in samples:
            legendEntry = samples[sample]['legend']
            isData = ('Data'  in legendEntry) and ('data' in Type)
            isSignal = ('Signal' in legendEntry) and ('sig' in Type)
            isBackground = ('Data' not in legendEntry) and ('Signal' not in legendEntry) and('bkg' in Type)
#            isFakes = ('Fakes' in legendEntry) and 'fakes' in Type

            if isData:
                stack[Type][legendEntry] = ROOT.THStack()
            elif isSignal:
                stack[Type][legendEntry] = ROOT.THStack()
            elif isBackground :
                stack[Type][legendEntry] = ROOT.THStack()
 #           elif isFakes :
 #               stack[Type][legendEntry] = ROOT.THStack()
    return stack

def fill_sample_stack(variable,trees,stack,samples,nbins,xmin,xmax):
    import ROOT
    from plotstyletools import set_sample_style
    from plotter import get_parser
    from variabletools import get_variables
    variables = get_variables()
    args = get_parser()
    for sample in samples:
        type = samples[sample]['type']
        legendEntry = samples[sample]['legend']

        label = type + sample + legendEntry + variables[variable]['name']
        temphist = ROOT.TH1F(label, label, nbins, xmin, xmax)
        temphist = set_sample_style(temphist, sample, samples)
        selection = get_selection(type, args.region)

        cmd = variable + ">>" + label
        print(cmd)
        trees[sample].Draw(cmd, selection)

        stack[type][legendEntry].Add(temphist.Clone())
        del temphist
    return stack

def get_selection(type,region):
    from regiontools import get_regionSelections

    unweighted_selection = get_regionSelections(region)
    weight = "1"
    if 'bkg' in type: weight = "36.2*trigSf*pupw_multi*eventweight_multi"
    passedTrigger = "passDilepTrigOR"

    if 'data' in type and (region.lower().startswith("blind") or region.lower().startswith("sr")): 
        print("blinded data for " + region)
        weight = "0"
    selection = passedTrigger + "*" + weight + "*(" + unweighted_selection +")"
    return selection 


def postprocess_stack(stack):
    """
    processStack Returns a Dictionary of THStacks, for the data and backgrounds 

    This function combines the variables samples, into single THStack objects 
    to be plotted under a given Legend Entry. 

    Note: breakdowns are not implemented properly 
    Args:
        stack (Dict(ROOT.THStack)): _description_
    Returns:
        samples (Dict) :
        breakdowns(Dict): yields and histograms 

    """
    import ROOT
    import math
    data                = ROOT.THStack()
    backgrounds         = ROOT.THStack()
    signals             = ROOT.THStack()

    backgrounds_zeroed  = ROOT.THStack()
    signals_zeroed      = ROOT.THStack()

    databreakdown       = {}
    backgroundbreakdown = {}
    signalbreakdown     = {}
    breakdowns          = {}
    samples             = {}
#    if state['BLINDED']: oklist = ['bkg','fakes','sig']
#    else: oklist = ['data','bkg','fakes','sig']
    oklist = ['data','bkg','fakes','sig']
    for Type in oklist:
        for legend  in stack[Type]:
            #tempyield = stack[Type][legend].GetStack().Last().Clone().integral(overflow=True,error=True)[0]
            #temperror = stack[Type][legend].GetStack().Last().Clone().integral(overflow=True,error=True)[1]
            tempyield = stack[Type][legend].GetStack().Last().Clone().Integral()
            #arg2 = ctypes.c_double(1000)
            #temperror = stack[Type][legend].GetStack().Last().Clone().IntegralAndError(0,30000, arg2, "I")#,error=True)[1]#,overflow=True
            temperror = 0 
            if Type == 'data':
                data.Add(stack[Type][legend].GetStack().Last().Clone())
                databreakdown[legend] = {'histogram': stack[Type][legend].GetStack().Last().Clone() ,'yield': tempyield, 'error': temperror }
            elif (Type == 'bkg') :
                backgrounds.Add(stack[Type][legend].GetStack().Last().Clone())
                backgroundbreakdown[legend] = {'histogram': stack[Type][legend].GetStack().Last().Clone() ,'yield': tempyield, 'error': temperror }
            elif (Type == 'fakes'):
                backgrounds.Add(stack[Type][legend].GetStack().Last().Clone())
                backgroundbreakdown[legend] = {'histogram': stack[Type][legend].GetStack().Last().Clone() ,'yield': tempyield, 'error': temperror }
            elif Type == 'sig':
                signals.Add(stack[Type][legend].GetStack().Last().Clone())
                signalbreakdown[legend] = {'histogram': stack[Type][legend].GetStack().Last().Clone() ,'yield': tempyield, 'error': temperror }
    totalyield = 0.0
    totalerror = 0.0
    for bkg in backgrounds:
        if bkg == "total": continue
        tempyield = bkg.Integral()
        #temperror = bkg.IntegralAndError(0,30000)
        temperror = 0 
        if tempyield < 0.0:
            tempyield = 0.0
        totalyield += tempyield
        totalerror += temperror**2
    totalerror = math.sqrt(totalerror)
    backgroundbreakdown['total'] = {'histogram': backgrounds.GetStack().Last().Clone(), 'yield':totalyield,'error':totalerror}


    breakdowns['background'] = backgroundbreakdown
    breakdowns['data']       = databreakdown
    breakdowns['signal']     = signalbreakdown
    samples['background'] = backgrounds
    samples['data'] = data
    samples['signal'] = signals
    return samples,breakdowns




def getPoissonCI(n, P = 0.68269):
    """
    getPoissonCI This function takes a number of events and returns the
     confidence interval [low, up] for the mean of the Poisson distribution.
     By default it returns the one sigma confidence interval.
    Args:
        n (float): The (observed) number of events
        P (float): Probability level for the (two-sided) interval

    Returns:
        limits (array of floats): [lower limit, upper limit]
    """
    import ROOT
    limits = []
    halfgamma = (1. - P) / 2.
    if n > 0:
        limits.append(ROOT.TMath.ChisquareQuantile(halfgamma, 2. * n) / 2.)
        limits.append(ROOT.TMath.ChisquareQuantile(1 - halfgamma, 2. * (n + 1)) / 2.)
    else:
        limits.append(0.)
        limits.append(-ROOT.TMath.Log(1 - halfgamma))

    return limits

def getDataGraph(suppresszero = True):
    """
    getDataGraph This function returns a TGraphAsymmErrors containing the data
     event yield with the associated poisson uncertainty.
    """
    from ctypes import c_double
    import ROOT
    dstack = data.GetStack().Last()
    nbins = dstack.GetNbinsX()
    vx = vy = vexl = vexh = veyl = veyh = []

    for i in range(1, nbins + 1):
        obs = dstack.GetBinContent(i)
        if supresszero and obs < 1.:
            continue

        limits = getPoissonCI(obs)
        vx.append(dstack.GetBinCenter(i))
        vy.append(obs)
        vexl.append(0.)
        vexh.append(0.)
        veyl.append(obs - limits[0])
        veyh.append(limits[1] - obs)

    dataGraph = ROOT.TGraphAsymmErrors(len(vx),
                    (c_double * len(vx))(*vx), (c_double * len(vy))(*vy),
                    (c_double * len(vexl))(*vexl), (c_double * len(vexh))(*vexh),
                    (c_double * len(veyl))(*veyl), (c_double * len(veyh))(*veyh))
    dataGraph.SetLineWidth(2.)

    return dataGraph

