void co60() {

    TFile *f = new TFile("co60.root","RECREATE");
    TTree *t = new TTree("t","Co60 source");

    double E;
    t->Branch("E",&E,"E/D");

    int N = 100000;

    for(int i=0; i<N; i++){
        if(gRandom->Rndm() < 0.5)
            E = 1.17;  // MeV
        else
            E = 1.33;  // MeV

        t->Fill();
    }

    t->Write();
    f->Close();
}
