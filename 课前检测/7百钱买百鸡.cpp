# include "iostream"
using namespace std;
int main(){
	int x,y;
	float n=1/3;
	for(int i=0;i<=20;i++){//假设公鸡i只 
		for(int x=0;x<=33;x++){//假设母鸡x只 
			y=100-x-i;
            if((x+y+i)==100 && (5*i+3*x+y/3)==100&&y%3==0){//同时要满足z是3的整数
				cout<<"公鸡"<<i<<"只"<<endl;
				cout<<"母鸡"<<x<<"只"<<endl;
				cout<<"小鸡"<<y<<"只"<<endl<<endl;
			}
		}
	}	
} 


//	8分
//	方程组的解 
//	9分
