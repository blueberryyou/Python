# include "iostream"
using namespace std;
int main(){
	int x,sign=1;
	cin>>x;
	if(x==1)
	cout<<"yes";
	else{
		for(int i=2;i<=x/2;i++){
		if(x%i==0){
			cout<<"no";
			sign=0;
			}
		}
		if(sign==1)
		cout<<"yes"; 
	} 
}

//	8分
//	素数的知识点 
//	8分
