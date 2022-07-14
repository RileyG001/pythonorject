#include "SimpleAnalysisFramework/AnalysisClass.h"

DefineAnalysis(VBS)

float ptMassCalc(auto bjet, auto cand)
{
  float M = sqrt(bjet.Pt() * cand.Pt() * (cosh(bjet.Eta()-cand.Eta()) - cos(bjet.Phi()-cand.Phi())));
  return M;
}

void VBS::Init()
{
  //addRegions({"loose"});
  addRegions({
    "Cutflow_Presel_0",
    "Cutflow_Presel_1_BadJetVeto",
    "Cutflow_Presel_2_NBaseLeptons",
    "Cutflow_Presel_3_NSignalLeptons",
    "Cutflow_Presel_4_NbJets",
    "Cutflow_Presel_5_NVBSJets",
  });

  addHistogram("meff_incl",200,0,2000);
  addHistogram("meff_4j",200,0,2000);
  addHistogram("met",100,0,1000);
  addHistogram("met_phi",80,-4,4);
  addHistogram("mTb_min",100,0,1000);
  addHistogram("mCT_bb",100,0,1000);
  addHistogram("dphi_min",40,0,4);
  addHistogram("dphi_1jet",40,0,4);
  addHistogram("m_bb",200,0,1000);
  addHistogram("m_non_bb",200,0,1000);
  addHistogram("ZCR_meff_4j",200,0,2000);
  addHistogram("ZCR_met",100,0,1000);
  addHistogram("Z_mass",200,0,1000);

  addHistogram("pt_lep_1",200,0,1000);
  addHistogram("pt_lep_2",200,0,1000);
  addHistogram("eta_lep_1",80,-4,4);
  addHistogram("eta_lep_2",80,-4,4);
  addHistogram("phi_lep_1",80,-4,4);
  addHistogram("phi_lep_2",80,-4,4);

  addHistogram("dR_l1_l2",50,0,12); //added by me!
  
  addHistogram("pt_jet_1",200,0,2000);
  addHistogram("pt_jet_2",200,0,2000);
  addHistogram("pt_jet_3",200,0,2000);
  addHistogram("pt_jet_4",200,0,2000);
  addHistogram("pt_jet_5",200,0,2000);
  addHistogram("pt_jet_6",200,0,2000);
  addHistogram("eta_jet_1",80,-5,5);
  addHistogram("eta_jet_2",80,-5,5);
  addHistogram("eta_jet_3",80,-5,5);
  addHistogram("eta_jet_4",80,-5,5);
  addHistogram("eta_jet_5",80,-5,5);
  addHistogram("eta_jet_6",80,-5,5);

  addHistogram("phi_jet_1",80,-4,4);
  addHistogram("phi_jet_2",80,-4,4);

  addHistogram("pt_bjet_1",200,0,2000);
  addHistogram("pt_bjet_2",200,0,2000);
  addHistogram("pt_bjet_3",200,0,2000);
  addHistogram("pt_bjet_4",200,0,2000);

  addHistogram("jets_n", 20, -0.5, 19.5);
  addHistogram("bjets_n",20, -0.5, 19.5);
  addHistogram("signal_electrons_n", 20, -0.5, 19.5);
  addHistogram("signal_muons_n", 20, -0.5, 19.5);
  addHistogram("signal_taus_n", 20, -0.5, 19.5);
  addHistogram("signal_leptons_n", 20, -0.5, 19.5);
  addHistogram("baseline_electrons_n", 20, -0.5, 19.5);
  addHistogram("baseline_muons_n", 20, -0.5, 19.5);
  addHistogram("baseline_taus_n", 20, -0.5, 19.5);
  addHistogram("baseline_leptons_n", 20, -0.5, 19.5);

  addHistogram("gen_filt_met",200,0,2000);
  addHistogram("gen_filt_ht",200,0,2000);

  addHistogram("mc_weight", 1, 0, 1);


  addHistogram("dR_j1_j2",50,0,12); //added by me!
  addHistogram("dR_j1_j3",50,0,12); //added by me!
  addHistogram("dR_j1_j4",50,0,12); //added by me!
  addHistogram("dR_j1_j5",50,0,12); //added by me!
  addHistogram("dR_j1_j6",50,0,12); //added by me!
  addHistogram("dR_j2_j3",50,0,12); //added by me!
  addHistogram("dR_j2_j4",50,0,12); //added by me!
  addHistogram("dR_j2_j5",50,0,12); //added by me!
  addHistogram("dR_j2_j6",50,0,12); //added by me!
  addHistogram("dR_j3_j4",50,0,12); //added by me!
  addHistogram("dR_j3_j5",50,0,12); //added by me!
  addHistogram("dR_j3_j6",50,0,12); //added by me!
  addHistogram("dR_j4_j5",50,0,12); //added by me!
  addHistogram("dR_j4_j6",50,0,12); //added by me!
  addHistogram("dR_j5_j6",50,0,12); //added by me!

  addHistogram("dR_bj1_bj2",50,0,12); //added by me!
  addHistogram("dR_bj1_bj3",50,0,12); //added by me!
  addHistogram("dR_bj1_bj4",50,0,12); //added by me!
  addHistogram("dR_bj2_bj3",50,0,12); //added by me!
  addHistogram("dR_bj2_bj4",50,0,12); //added by me!
  addHistogram("dR_bj3_bj4",50,0,12); //added by me!

  addHistogram("pt_vbsjet_1", 200,0,2000); //added by me!
  addHistogram("pt_vbsjet_2", 200,0,2000);
  addHistogram("eta_vbsjet_1", 80,-5,5); 
  addHistogram("eta_vbsjet_2", 80,-5,5);
  addHistogram("phi_vbsjet_1", 80,-4,4);
  addHistogram("phi_vbsjet_2", 80,-4,4);
  addHistogram("dR_vbs_j1_j2", 80,0,12);



  //#ifdef PACKAGE_BTaggingTruthTagging
  //#pragma message "Compiling BTaggingTruthTagging for TRF usage"
  //m_btt = new BTaggingTruthTaggingTool("MyBTaggingTruthTaggingTool");
  //StatusCode code = m_btt->setProperty("TaggerName", "MV2c10");
  //if (code != StatusCode::SUCCESS) throw std::runtime_error("error setting BTaggingTruthTaggingTool TaggerName property");
  //code = m_btt->setProperty("OperatingPoint", "FixedCutBEff_77");
  //if (code != StatusCode::SUCCESS) throw std::runtime_error("error setting BTaggingTruthTaggingTool OperatingPoint property");
  //code = m_btt->setProperty("JetAuthor", "AntiKt4EMTopoJets");
  //if (code != StatusCode::SUCCESS) throw std::runtime_error("error setting BTaggingTruthTaggingTool JetAuthor property");
  //code = m_btt->setProperty("ScaleFactorFileName", "xAODBTaggingEfficiency/13TeV/2016-20_7-13TeV-MC15-CDI-2017-06-07_v2.root");
  //if (code != StatusCode::SUCCESS) throw std::runtime_error("error setting BTaggingTruthTaggingTool ScaleFactorFileName property");
  // call initialize() function
  //code = m_btt->initialize();
  //if (code != StatusCode::SUCCESS) throw std::runtime_error("error initializing the BTaggingTruthTaggingTool");
  //std::cout << "Initialized BTaggingTruthTagging tool" << std::endl;
  //#endif

}

static int jetFlavor(AnalysisObject &jet) {
  if (jet.pass(TrueBJet)) return 5;
  if (jet.pass(TrueCJet)) return 4;
  if (jet.pass(TrueTau)) return 15;
  return 0;
}

void VBS::ProcessEvent(AnalysisEvent *event)
{

  float gen_filt_met = event->getGenMET();
  float gen_filt_ht  = event->getGenHT();
  int channel_number = event->getMCNumber();

  fill("mc_weight", event->getMCWeights()[0]);

  // baseline electrons are requested to pass the loose likelihood identification criteria
  //    and have pT > 20 GeV and |eta| < 2.47
  auto electrons  = event->getElectrons(10, 2.47, ELooseLH);
  // baseline muons are required to pass the Medium selections and to have pT > 20 GeV, |eta| < 2.5
  auto muons      = event->getMuons(10, 2.7, MuMedium);
  // small-R jets: pT > 20 GeV, |eta| < 2.8
  auto taus       = event->getTaus(20, 2.5, TauRNNLoose);

  auto candJets   = event->getJets(20., 4.5);
  auto metVec     = event->getMET();

  double met      = metVec.Et();
  double met_phi  = metVec.Phi();

  // No bad muon veto implemented

  // Overlap removal
  auto radiusCalcJet  = [] (const AnalysisObject& , const AnalysisObject& muon) { return std::min(0.4, 0.04 + 10/muon.Pt()); };
  auto radiusCalcMuon = [] (const AnalysisObject& muon, const AnalysisObject& ) { return std::min(0.4, 0.04 + 10/muon.Pt()); };
  auto radiusCalcElec = [] (const AnalysisObject& elec, const AnalysisObject& ) { return std::min(0.4, 0.04 + 10/elec.Pt()); };
  auto radiusCalcTau = [] (const AnalysisObject& tau, const AnalysisObject& ) { return std::min(0.4, 0.04 + 10/tau.Pt()); };

  // apply JVT
  candJets = filterObjects(candJets, 20, 5, JVT50Jet);

  // apply overlap removal
  electrons  = overlapRemoval(electrons, muons, 0.01);
  candJets   = overlapRemoval(candJets, electrons, 0.2, NOT(BTag77MV2c10));
  electrons  = overlapRemoval(electrons, candJets, radiusCalcElec);
  candJets   = overlapRemoval(candJets, muons, radiusCalcJet, LessThan3Tracks);
  muons      = overlapRemoval(muons, candJets, radiusCalcMuon);
  ///Remove taus overlapping with electrons if dR<0.2




  taus = overlapRemoval(taus, electrons, 0.2);
  electrons =overlapRemoval(electrons, muons, 0.01);
  taus = overlapRemoval(taus, muons, 0.2);
  muons = overlapRemoval(muons, electrons, 0.1, NOT(MuCaloTaggedOnly));
  candJets= overlapRemoval(candJets, electrons, 0.01, BTag77MV2c10);
  electrons = overlapRemoval(electrons, candJets, radiusCalcJet);             //new stuff taffard asked for about removing overlap
  candJets = overlapRemoval(candJets, muons, radiusCalcJet, LessThan3Tracks);
  muons = overlapRemoval(muons, candJets, radiusCalcMuon);
  candJets = overlapRemoval(candJets, taus, 0.2);



  // No cosmic muon veto implemented

  // require signal jets to be 30 GeV
  auto signalJets      = filterObjects(candJets, 5);
  // signal electrons are required to pass the Medium likelihood criteria and isolated using LooseTrackOnly
  auto signalElectrons = filterObjects(electrons, 10, 2.47, ETightLH|ED0Sigma5|EZ05mm|EIsoBoosted);
  // signal muons are required to be isolated using LooseTrackOnly
  auto signalMuons     = filterObjects(muons, 10, 2.7, MuD0Sigma3|MuZ05mm|MuIsoBoosted|MuNotCosmic);
  auto signalTaus = filterObjects(taus, 20, 2.5, TauRNNLoose); 
  // combine into signalLeptons for easy counting
  auto signalLeptons   = signalElectrons + signalMuons + signalTaus;

  // get b-jets
  auto candBJets    = filterObjects(signalJets, 30., 5);
  auto bjets        = filterObjects(signalJets, 30., 5, BTag77MV2c10);
  auto nonbjets     = filterObjects(signalJets, 30., 5, NOT(BTag77MV2c10));

  int bjets_n       = bjets.size();
  //  int n_nonbjets    = nonbjets.size();
  int jets_n        = signalJets.size();
  int signal_electrons_n   = signalElectrons.size();
  int signal_muons_n       = signalMuons.size();
  int signal_taus_n       = signalTaus.size();
  int signal_leptons_n     = signalLeptons.size();

    // added by me! counting LooseBadJets
  //int nBadJets = countObjects(candJets, 20, 4.5, NOT(LooseBadJet));
  //if(countObjects(candJets, 20, 4.5, NOT(LooseBadJet))!=0) return;

  int baseline_electrons_n   = electrons.size();
  int baseline_muons_n       = muons.size();
  int baseline_taus_n       = taus.size();
  int baseline_leptons_n     = electrons.size()+muons.size()+taus.size();

  // require at least 4 signal jets
  if(jets_n < 4) return;


  
/*
  bool pass_presel_1 = false;

  accept("Cutflow_Presel_0");
  if(nBadJets==0)
 { 
    accept("Cutflow_Presel_1_BadJetVeto"),
    pass_presel_1 = true;
    /*if (baseline_leptons_n >= 2)
    {
      accept("Cutflow_Presel_2_NBaseLeptons")
      if (signal_leptons_n >= 2)
      {
        accept("Cutflow_Presel_3_NSignalLeptons")
        if ()
      }
    }

  }
  if(!pass_presel_1) return;

*/



//compiling code
  bool not_vbs_event = true; //need to invert logic and implement cut system
  float higgs_mass = 125.; //mass we are expecting the higgs to have
  float range = 20.; //allowed devation from the mass of the higgs in GeV

  if(bjets_n == 1){
    bool cand_bjet_set = false;//reverse logic
    auto cand_bjet = bjets[0]; //defaulted to bjets[0], if the conditions aren't met this is thrown away
    int cand_bjet_number;
    for(int i = 0; i < nonbjets.size(); i++){
      float mass_dev = fabs(higgs_mass - (bjets[0]+nonbjets[i]).M()); //comparing the combined mass against the mass of the higgs 
      if(mass_dev < range){
        range = mass_dev;
       // AnalysisObject cand_bjet = nonbjets[i];
        cand_bjet_number = i;
        cand_bjet_set = true; //allowing the code to complete
      }
    }
    if(cand_bjet_set){
      bjets.push_back(nonbjets[cand_bjet_number]);
      nonbjets.erase(nonbjets.begin()+cand_bjet_number);
    } //make this contain bjet.push_back() after the logic reversal; also do the cuts after 
    else{
      bool cut_flag = true; //this is where the cut/cutflag will go
    }
  }
  bjets_n = bjets.size(); //recalcing bjets_n to account for a new jet!

 //VBS jet detection algo
  AnalysisObjects vbsjets; //defining the vbsjets catagory
  float dEta_range = 5.5; //should be set around 4.5
  float check_dEta;
  bool cand_vbsjet_set = false;
  uint cand_vbsjet1_number, cand_vbsjet2_number;
  for(uint i = 0; i < nonbjets.size(); i++){
    for(uint j = i+1; j < nonbjets.size(); j++){
      check_dEta = fabs(nonbjets[i].Eta()-nonbjets[j].Eta());
      if(dEta_range < check_dEta){
        dEta_range = check_dEta;
        cand_vbsjet1_number = i;
        cand_vbsjet2_number = j;
        cand_vbsjet_set = true;
      }
    }
  }
  if(cand_vbsjet_set){
    vbsjets.push_back(nonbjets[cand_vbsjet1_number]); //storing our successful cands into vbsjets
    vbsjets.push_back(nonbjets[cand_vbsjet2_number]);
  }



  // inclusive meff - all jets + leptons
  float meff_incl = met + sumObjectsPt(signalJets) + sumObjectsPt(signalLeptons);
  // meff from 4 leading jets only
  float meff_4j = met + sumObjectsPt(signalJets, 4);
  // min mT of leading 3 bjets
  float mTb_min = -999;
  if (bjets.size()>0) mTb_min = calcMTmin(bjets, metVec);
  // min mCT_bb of leading 2 bjets
  float mCT_bb = -999;
  if (bjets.size()>1) mCT_bb = calcMCT(bjets[0], bjets[1]);
  // dphimin between leading 4 signal jets and met
  float dphi_min  = minDphi(metVec, signalJets, 4);
  // dPhi(j1, MET) for Gbb
  float dphi_1jet  = minDphi(metVec, signalJets, 1);
  // invariant mass of two leading b-tagged jets


  float m_bb = -999.;
  if (bjets.size()>1) m_bb = (bjets[0] + bjets[1]).M();
  // invariant mass of two leading non-b-tagged jets
  float m_non_bb = -999.;
  if (nonbjets.size()>1) m_non_bb = (nonbjets[0] + nonbjets[1]).M();

  // leading and subleading lepton pt
  float pt_lep_1 = -999;
  if (signalLeptons.size()>0) pt_lep_1 = signalLeptons[0].Pt();
  float pt_lep_2 = -999;
  if (signalLeptons.size()>1) pt_lep_2 = signalLeptons[1].Pt();

  // leading and subleading lepton eta
  float eta_lep_1 = -999;
  if (signalLeptons.size()>0) eta_lep_1 = signalLeptons[0].Eta();
  float eta_lep_2 = -999;
  if (signalLeptons.size()>1) eta_lep_2 = signalLeptons[1].Eta();

  // leading and subleading lepton phi
  float phi_lep_1 = -999;
  if (signalLeptons.size()>0) phi_lep_1 = signalLeptons[0].Phi();
  float phi_lep_2 = -999;
  if (signalLeptons.size()>1) phi_lep_2 = signalLeptons[1].Phi();

  float dR_l1_l2 = -999.;
  if (signalLeptons.size()>1) dR_l1_l2 = signalLeptons[0].DeltaR(signalLeptons[1]);

  float pt_vbsjet_1 = -999;
  float pt_vbsjet_2 = -999;
  float eta_vbsjet_1 = -999;
  float eta_vbsjet_2 = -999;
  float phi_vbsjet_1 = -999;
  float phi_vbsjet_2 = -999;
  float dR_vbs_j1_j2 = -999;
  if (vbsjets.size()>1){
    pt_vbsjet_1 = vbsjets[0].Pt();
    pt_vbsjet_2 = vbsjets[1].Pt();
    eta_vbsjet_1 = vbsjets[0].Eta();
    eta_vbsjet_2 = vbsjets[1].Eta();
    phi_vbsjet_1 = vbsjets[0].Phi();
    phi_vbsjet_2 = vbsjets[1].Phi();
    dR_vbs_j1_j2 = vbsjets[0].DeltaR(vbsjets[1]);
  } 




  // leading and subleading jet pt
  float pt_jet_1 = -999;
  if (nonbjets.size()>0) pt_jet_1 = nonbjets[0].Pt();
  float pt_jet_2 = -999;
  if (nonbjets.size()>1) pt_jet_2 = nonbjets[1].Pt();
  float pt_jet_3 = -999;
  if (nonbjets.size()>2) pt_jet_3 = nonbjets[2].Pt();
  float pt_jet_4 = -999;
  if (nonbjets.size()>3) pt_jet_4 = nonbjets[3].Pt();
  float pt_jet_5 = -999;
  if (nonbjets.size()>4) pt_jet_5 = nonbjets[4].Pt();
  float pt_jet_6 = -999;
  if (nonbjets.size()>5) pt_jet_6 = nonbjets[5].Pt();

  float dR_j1_j2 = -999; //me
  if (nonbjets.size()>1) dR_j1_j2 = nonbjets[0].DeltaR(nonbjets[1]);
  float dR_j1_j3 = -999; //me
  if (nonbjets.size()>2) dR_j1_j3= nonbjets[0].DeltaR(nonbjets[2]);
  float dR_j1_j4 = -999; //me
  if (nonbjets.size()>3) dR_j1_j4= nonbjets[0].DeltaR(nonbjets[3]);
  float dR_j1_j5 = -999; //me
  if (nonbjets.size()>4) dR_j1_j5= nonbjets[0].DeltaR(nonbjets[4]);
  float dR_j1_j6 = -999; //me
  if (nonbjets.size()>5) dR_j1_j6= nonbjets[0].DeltaR(nonbjets[5]);
  float dR_j2_j3 = -999; //me
  if (nonbjets.size()>2) dR_j2_j3= nonbjets[1].DeltaR(nonbjets[2]);
  float dR_j2_j4 = -999; //me 
  if (nonbjets.size()>3) dR_j2_j4= nonbjets[1].DeltaR(nonbjets[3]);
  float dR_j2_j5 = -999; //me
  if (nonbjets.size()>4) dR_j2_j5= nonbjets[1].DeltaR(nonbjets[4]);
  float dR_j2_j6 = -999; //me
  if (nonbjets.size()>5) dR_j2_j6= nonbjets[1].DeltaR(nonbjets[5]);
  float dR_j3_j4 = -999; //me 
  if (nonbjets.size()>3) dR_j3_j4= nonbjets[2].DeltaR(nonbjets[3]);
  float dR_j3_j5 = -999; //me
  if (nonbjets.size()>4) dR_j3_j5= nonbjets[2].DeltaR(nonbjets[4]);
  float dR_j3_j6 = -999; //me
  if (nonbjets.size()>5) dR_j3_j6= nonbjets[2].DeltaR(nonbjets[5]);
  float dR_j4_j5 = -999; //me
  if (nonbjets.size()>4) dR_j4_j5= nonbjets[3].DeltaR(nonbjets[4]);
  float dR_j4_j6 = -999; //me
  if (nonbjets.size()>5) dR_j4_j6= nonbjets[3].DeltaR(nonbjets[5]);
  float dR_j5_j6 = -999; //me
  if (nonbjets.size()>5) dR_j5_j6= nonbjets[4].DeltaR(nonbjets[5]);
//new stuff







  // leading and subleading bjet pt
  float pt_bjet_1 = -999;
  if (bjets.size()>0) pt_bjet_1 = bjets[0].Pt();
  float pt_bjet_2 = -999;
  if (bjets.size()>1) pt_bjet_2 = bjets[1].Pt();
  float pt_bjet_3 = -999;
  if (bjets.size()>2) pt_bjet_3 = bjets[2].Pt();
  float pt_bjet_4 = -999;
  if (bjets.size()>3) pt_bjet_4 = bjets[3].Pt();

  float dR_bj1_bj2 = -999; //me
  if (bjets.size()>1) dR_bj1_bj2 = bjets[0].DeltaR(bjets[1]);
  float dR_bj1_bj3 = -999; //me
  if (bjets.size()>2) dR_bj1_bj3 = bjets[0].DeltaR(bjets[2]);
  float dR_bj1_bj4 = -999; //me
  if (bjets.size()>3) dR_bj1_bj4 = bjets[0].DeltaR(bjets[3]);
  float dR_bj2_bj3 = -999; //me
  if (bjets.size()>2) dR_bj2_bj3 = bjets[1].DeltaR(bjets[2]);
  float dR_bj2_bj4 = -999; //me
  if (bjets.size()>3) dR_bj2_bj4 = bjets[1].DeltaR(bjets[3]);
  float dR_bj3_bj4 = -999; //me
  if (bjets.size()>3) dR_bj3_bj4 = bjets[2].DeltaR(bjets[3]);


  // leading and subleading jet eta
  float eta_jet_1 = -999;
  if (nonbjets.size()>0) eta_jet_1 = nonbjets[0].Eta();
  float eta_jet_2 = -999;
  if (nonbjets.size()>1) eta_jet_2 = nonbjets[1].Eta();

  float eta_jet_3 = -999;
  if (nonbjets.size()>2) eta_jet_3 = nonbjets[2].Eta();
  float eta_jet_4 = -999;
  if (nonbjets.size()>3) eta_jet_4 = nonbjets[3].Eta();

  float eta_jet_5 = -999;
  if (nonbjets.size()>4) eta_jet_5 = nonbjets[4].Eta();
  float eta_jet_6 = -999;
  if (nonbjets.size()>5) eta_jet_6 = nonbjets[5].Eta();



  // leading and subleading jet phi
  float phi_jet_1 = -999;
  if (nonbjets.size()>0) phi_jet_1 = nonbjets[0].Phi();
  float phi_jet_2 = -999;
  if (nonbjets.size()>1) phi_jet_2 = nonbjets[1].Phi();

  // Z+jets CR info
  TLorentzVector tlv_Z;
  if((signal_electrons_n == 2) && (signal_muons_n < 1)) {
    tlv_Z = signalElectrons[0]+signalElectrons[1];
  }
  if((signal_muons_n == 2) && (signal_electrons_n < 1)) {
    tlv_Z = signalMuons[0]+signalMuons[1];
  }

  float Z_pt = tlv_Z.Pt();
  float Z_phi = tlv_Z.Phi();
  float Z_mass = tlv_Z.M();

  TVector2 tv2_met; tv2_met.SetMagPhi(met, metVec.Phi());
  TVector2 tv2_Z; tv2_Z.SetMagPhi(Z_pt, Z_phi);
  TVector2 total = tv2_met+tv2_Z;

  float ZCR_met = total.Mod();
  float ZCR_meff_4j = ZCR_met + sumObjectsPt(signalJets, 4);

//the new stuff will go here
\


  fill("meff_incl", meff_incl);
  fill("meff_4j", meff_4j);
  fill("met", met);
  fill("met_phi", met_phi);
  fill("mTb_min", mTb_min);
  fill("mCT_bb", mCT_bb);
  fill("dphi_min", dphi_min);
  fill("dphi_1jet", dphi_1jet);
  fill("m_bb", m_bb);
  fill("m_non_bb", m_non_bb);
  fill("pt_lep_1",pt_lep_1);
  fill("pt_lep_2",pt_lep_2);
  fill("eta_lep_1",eta_lep_1);
  fill("eta_lep_2",eta_lep_2);
  fill("phi_lep_1",phi_lep_1);
  fill("phi_lep_2",phi_lep_2);
  fill("dR_l1_l2",dR_l1_l2); //made by me

  fill("ZCR_meff_4j", ZCR_meff_4j);
  fill("ZCR_met", ZCR_met);
  fill("Z_mass", Z_mass);

  fill("pt_jet_1", pt_jet_1);
  fill("pt_jet_2", pt_jet_2);
  fill("pt_jet_3", pt_jet_3);
  fill("pt_jet_4", pt_jet_4);
  fill("pt_jet_5", pt_jet_5);
  fill("pt_jet_6", pt_jet_6);

  fill("eta_jet_1", eta_jet_1);
  fill("eta_jet_2", eta_jet_2);
  fill("eta_jet_3", eta_jet_3);
  fill("eta_jet_4", eta_jet_4);
  fill("eta_jet_5", eta_jet_5);
  fill("eta_jet_6", eta_jet_6);

  fill("phi_jet_1", phi_jet_1);
  fill("phi_jet_2", phi_jet_2);

  fill("dR_j1_j2",dR_j1_j2); //made by me
  fill("dR_j1_j3",dR_j1_j3); //made by me  
  fill("dR_j1_j4",dR_j1_j4); //made by me  
  fill("dR_j1_j5",dR_j1_j5); //made by me  
  fill("dR_j1_j6",dR_j1_j6); //made by me  
  fill("dR_j2_j3",dR_j2_j3); //made by me  
  fill("dR_j2_j4",dR_j2_j4); //made by me
  fill("dR_j2_j5",dR_j2_j5); //made by me  
  fill("dR_j2_j6",dR_j2_j6); //made by me  
  fill("dR_j3_j4",dR_j3_j4); //made by me  
  fill("dR_j3_j5",dR_j3_j5); //made by me  
  fill("dR_j3_j6",dR_j3_j6); //made by me  
  fill("dR_j4_j5",dR_j4_j5); //made by me
  fill("dR_j4_j6",dR_j4_j6); //made by me  
  fill("dR_j5_j6",dR_j5_j6); //made by me  





  fill("pt_bjet_1", pt_bjet_1);
  fill("pt_bjet_2", pt_bjet_2);
  fill("pt_bjet_3", pt_bjet_3);
  fill("pt_bjet_4", pt_bjet_4);

  fill("dR_bj1_bj2",dR_bj1_bj2); //made by me
  fill("dR_bj1_bj3",dR_bj1_bj3); //made by me  
  fill("dR_bj1_bj4",dR_bj1_bj4); //made by me 
  fill("dR_bj2_bj3",dR_bj2_bj3); //made by me
  fill("dR_bj2_bj4",dR_bj2_bj4); //made by me  
  fill("dR_bj3_bj4",dR_bj3_bj4); //made by me  


  fill("jets_n", jets_n);
  fill("bjets_n", bjets_n);
  fill("signal_electrons_n", signal_electrons_n);
  fill("signal_muons_n", signal_muons_n);
  fill("signal_taus_n", signal_taus_n);
  fill("signal_leptons_n", signal_leptons_n);
  fill("baseline_electrons_n", baseline_electrons_n);
  fill("baseline_taus_n", baseline_taus_n);
  fill("baseline_muons_n", baseline_muons_n);
  fill("baseline_leptons_n", baseline_leptons_n);

  fill("pt_vbsjet_1", pt_vbsjet_1); //added by me!
  fill("pt_vbsjet_2", pt_vbsjet_2);
  fill("eta_vbsjet_1", eta_vbsjet_1);
  fill("eta_vbsjet_2", eta_vbsjet_2);
  fill("phi_vbsjet_1", phi_vbsjet_1); 
  fill("phi_vbsjet_2", phi_vbsjet_2); 
  fill("dR_vbs_j1_j2", dR_vbs_j1_j2); 


  // loose preselection
  //  if(jets_n >= 4 && met > 200 && dphi_min > 0.4 && meff_4j > 700){
  ///      accept("loose");
  //      if(baseline_leptons_n == 0)
  //        accept("loose_0l");
  //  }
  accept("loose");
  // SRs, CRs, and VRs selections 
	/*
  if(jets_n >= 4 && bjets_n >= 2 && met > 200 && dphi_min > 0.4 && meff_4j > 700){
    accept("medium");
    if(bjets_n == 2 && jets_n <= 5)
      accept("tight");
    // 0L
    if(baseline_leptons_n == 0){
      accept("medium_0l");
      if(bjets_n == 2 && jets_n <= 5) {
        accept("tight_0l");
        // SRs
        if(m_bb > 105 && m_bb < 135 && m_non_bb > 75 && m_non_bb < 90){
          // SR1
          if(jets_n == 4 && meff_4j > 900 && mTb_min > 140 && mCT_bb > 140) accept("SR1");
          // SR2
          if(jets_n <= 5 && meff_4j > 900 && met > 250 && mTb_min > 160 && mCT_bb > 140) accept("SR2");
          // SR3
          if(jets_n <= 5 && meff_4j > 700 && mTb_min > 180 && mCT_bb > 190) accept("SR3");
        }//end SRs
        // CRs ttbar
        if(m_bb > 135 && m_non_bb > 75 && m_non_bb < 90 && mTb_min < 140 && mCT_bb < 140){
          // CR1tt
          if(jets_n == 4 && meff_4j > 900) accept("CR1tt");
          // CR2tt
          if(jets_n <= 5 && meff_4j > 900 && met > 250) accept("CR2tt");
          // CR3tt
          if(jets_n <= 5 && meff_4j > 700) accept("CR3tt");
        }//end CRs ttbar
        // VRs ttbar
        if(m_bb > 135 && m_non_bb > 75 && m_non_bb < 90){
          // VR1tt
          if(jets_n == 4 && meff_4j > 900 && mTb_min > 140 && mCT_bb < 140) accept("VR1tt_mbb_mct");
          // VR2tt
          if(jets_n <= 5 && meff_4j > 900 && met > 250 && mTb_min > 160 && mCT_bb < 140) accept("VR2tt_mbb_mct");
          // VR3tt
          if(jets_n <= 5 && meff_4j > 700 && mTb_min > 180 && mCT_bb < 190) accept("VR3tt_mbb_mct");
        }//end VRs ttbar
        // VRs SB-bb, SB-nonbb
        if((m_bb < 105 || m_bb > 135) && (m_non_bb < 75 || m_non_bb > 90)){
          // SR1
          if(jets_n == 4 && meff_4j > 900 && mTb_min > 140 && mCT_bb > 140) accept("VR1_SBbb_SBqq");
          // SR2
          if(jets_n <= 5 && meff_4j > 900 && met > 250 && mTb_min > 160 && mCT_bb > 140) accept("VR2_SBbb_SBqq");
          // SR3
          if(jets_n <= 5 && meff_4j > 700 && mTb_min > 180 && mCT_bb > 190) accept("VR3_SBbb_SBqq");
        }//end VRs SB-bb, SB-nonbb
        // VRs SB-bb-high
        if(m_bb > 135 && m_non_bb > 75 && m_non_bb < 90){
          // SR1
          if(jets_n == 4 && meff_4j > 900 && mTb_min > 140 && mCT_bb > 140) accept("VR1_SBbbhigh");
          // SR2
          if(jets_n <= 5 && meff_4j > 900 && met > 250 && mTb_min > 160 && mCT_bb > 140) accept("VR2_SBbbhigh");
          // SR3
          if(jets_n <= 5 && meff_4j > 700 && mTb_min > 180 && mCT_bb > 190) accept("VR3_SBbbhigh");
        }//end VRs SB-bb, SB-nonbb
      }//end 2b
    }//end 0L
    // CRs singletop (1L)
    if((signal_electrons_n == 1 || signal_muons_n == 1) && bjets_n == 2 && jets_n <= 5 && meff_4j > 700 && m_bb > 195 && m_non_bb > 75 && m_non_bb < 90 && mTb_min > 180 && mCT_bb > 200){
      // CR1 (and 3)
      accept("CR1top");
      accept("CR3top");
      // CR2 singletop
      if(met > 250) accept("CR2top");
    }//end CRs singletop
    // CRs Zjets (2L SF)
    if((signal_electrons_n == 2 || signal_muons_n == 2) && pt_lep_1 > 140 && pt_lep_2 > 20 && bjets_n == 2 && jets_n <= 5 && m_bb > 200 && Z_mass > 75 && Z_mass < 105){
      // CR1 Zjets
      if(meff_4j > 900) accept("CR1Z");
      // CR2 Zjets
      if(meff_4j > 900 && met > 250) accept("CR2Z");
      // CR3 Zjets
      if(meff_4j > 700) accept("CR3Z");
    }//end CRs Zjets
  }
	*/
  ntupVar("mc_weight", event->getMCWeights()[0]);

  ntupVar("gen_filt_met", gen_filt_met);
  ntupVar("gen_filt_ht", gen_filt_ht);
  ntupVar("channel_number", channel_number);

  ntupVar("meff_incl", meff_incl);
  ntupVar("meff_4j", meff_4j);
  ntupVar("met", met);
  ntupVar("met_phi", met_phi);
  ntupVar("mTb_min", mTb_min);
  ntupVar("mCT_bb", mCT_bb);
  ntupVar("dphi_min", dphi_min);
  ntupVar("dphi_1jet", dphi_1jet);
  ntupVar("m_bb", m_bb);
  ntupVar("m_non_bb", m_non_bb);
  ntupVar("pt_lep_1",pt_lep_1);
  ntupVar("pt_lep_2",pt_lep_2);
  ntupVar("eta_lep_1",eta_lep_1);
  ntupVar("eta_lep_2",eta_lep_2);
  ntupVar("phi_lep_1",phi_lep_1);
  ntupVar("phi_lep_2",phi_lep_2);
  ntupVar("dR_l1_l2",dR_l1_l2); //made by me
  ntupVar("ZCR_meff_4j", ZCR_meff_4j);
  ntupVar("ZCR_met", ZCR_met);
  ntupVar("Z_mass", Z_mass);

  ntupVar("pt_jet_1", pt_jet_1);
  ntupVar("pt_jet_2", pt_jet_2);
  ntupVar("pt_jet_3", pt_jet_3);
  ntupVar("pt_jet_4", pt_jet_4);
  ntupVar("pt_jet_5", pt_jet_5);
  ntupVar("pt_jet_6", pt_jet_6);

  ntupVar("eta_jet_1",eta_jet_1);
  ntupVar("eta_jet_2",eta_jet_2);
  ntupVar("phi_jet_1",phi_jet_1);
  ntupVar("phi_jet_2",phi_jet_2);

  ntupVar("dR_j1_j2",dR_j1_j2); //me
  ntupVar("dR_j1_j3",dR_j1_j3);
  ntupVar("dR_j1_j4",dR_j1_j4);
  ntupVar("dR_j1_j5",dR_j1_j5);
  ntupVar("dR_j1_j6",dR_j1_j6);
  ntupVar("dR_j2_j3",dR_j2_j3);
  ntupVar("dR_j2_j4",dR_j2_j4);
  ntupVar("dR_j2_j5",dR_j2_j5);
  ntupVar("dR_j2_j6",dR_j2_j6);
  ntupVar("dR_j3_j4",dR_j3_j4);
  ntupVar("dR_j3_j5",dR_j3_j5);
  ntupVar("dR_j3_j6",dR_j3_j6);
  ntupVar("dR_j4_j5",dR_j4_j5);
  ntupVar("dR_j4_j6",dR_j4_j6);
  ntupVar("dR_j5_j6",dR_j5_j6);

  ntupVar("pt_bjet_1", pt_bjet_1);
  ntupVar("pt_bjet_2", pt_bjet_2);
  ntupVar("pt_bjet_3", pt_bjet_3);
  ntupVar("pt_bjet_4", pt_bjet_4);

  ntupVar("dR_bj1_bj2",dR_bj1_bj2); //me
  ntupVar("dR_bj1_bj3",dR_bj1_bj3);
  ntupVar("dR_bj1_bj4",dR_bj1_bj4);
  ntupVar("dR_bj2_bj3",dR_bj2_bj3); //me
  ntupVar("dR_bj2_bj4",dR_bj2_bj4);
  ntupVar("dR_bj3_bj4",dR_bj3_bj4);

  ntupVar("jets_n", jets_n);
  ntupVar("bjets_n", bjets_n);
  ntupVar("baseline_electrons_n", static_cast<int>(electrons.size()));
  ntupVar("baseline_muons_n", static_cast<int>(muons.size()));
  ntupVar("baseline_leptons_n", static_cast<int>(electrons.size()+muons.size()));
  ntupVar("signal_electrons_n", static_cast<int>(signalElectrons.size()));
  ntupVar("signal_muons_n", static_cast<int>(signalMuons.size()));
  ntupVar("signal_leptons_n", signal_leptons_n);

  ntupVar("signalJe:s0_pass_BTag77MV2c10", signalJets[0].pass(BTag77MV2c10));
  ntupVar("signalJets0_Pt", signalJets[0].Pt());
  ntupVar("signalJets3_Pt", signalJets[3].Pt());

  ntupVar("truth_id0", jetFlavor(signalJets[0]));
  ntupVar("truth_id1", jetFlavor(signalJets[1]));
  ntupVar("truth_id2", jetFlavor(signalJets[2]));
  ntupVar("truth_id3", jetFlavor(signalJets[3]));

  //#ifdef PACKAGE_BTaggingTruthTagging
  //  ntupVar("weight_2b_in", m_TTres.map_trf_weight_in["Nominal"].at(2));
  //  ntupVar("weight_2b_ex", m_TTres.map_trf_weight_ex["Nominal"].at(2));
  //#endif

  return;
}
