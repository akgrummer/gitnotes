//Save code as test.cpp file and run as root -l test.cpp+
#include <TCanvas.h>
#include <TH1D.h>
#include <TThread.h>
#include <TRandom.h>

void *filler(void *hist) {
	TH1D* h = (TH1D*)hist;
	for ( int i = 0; i < 1000000; i++ ) {
		usleep(10000);
		h->Fill(gRandom->Gaus(5,1));
	}
	return NULL;
}

void test()
{
	TCanvas* c = new TCanvas();
	c->SetLogy();
	TH1D * h = new TH1D("h", "h", 100, 0, 10);
	h->Draw();

	TThread *filler_t=new TThread("filler_thread",filler,(void*)h);
	filler_t->Run();
}
