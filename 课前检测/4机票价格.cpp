# include "iostream"
using namespace std;
int main(){
	int month,num,sum;
	cin>>month>>num;
	if(month>=7&&month<=9){
		if(num>=20){
			sum=num*3000*0.85;
		}else{
			sum=num*3000*0.95;
		}
	}else if(month==6||month==12){
		sum=num*3000*0.9;
	}else{
		if(num>=20){
			sum=num*3000*0.7;
		}else{
			sum=num*3000*0.8;
		}
	}
	cout<<sum<<"元";
}

//	8分
//	if、else的使用
//	9分

