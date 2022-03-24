# include "iostream"
using namespace std;
int main(){
	for(int i=100;i<=999;i++){
		if(i==(i%10)*(i%10)*(i%10)+(i/10%10)*(i/10%10)*(i/10%10)+(i/100)*(i/100)*(i/100))
		cout<<i<<"\t"; 
	}
}

//	8分
//	%、/的区别  
//9分	
