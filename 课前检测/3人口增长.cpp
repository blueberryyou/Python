# include "iostream"
using namespace std;
int main(){
	double x,i;
	x=12.9533;
	for(int i=1;;i++){
		x=x*(1+0.0107); 
		if(x>=15){
			cout<<i<<"年后，我国人口达到或超过15亿。"; 
			return 0; 
		} 
	}
}

//	9分
//	累乘的运用
//10fen 
