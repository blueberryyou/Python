# include "iostream"
using namespace std;
int main(){
	int x,y;
	float n=1/3;
	for(int i=0;i<=20;i++){//���蹫��iֻ 
		for(int x=0;x<=33;x++){//����ĸ��xֻ 
			y=100-x-i;
            if((x+y+i)==100 && (5*i+3*x+y/3)==100&&y%3==0){//ͬʱҪ����z��3������
				cout<<"����"<<i<<"ֻ"<<endl;
				cout<<"ĸ��"<<x<<"ֻ"<<endl;
				cout<<"С��"<<y<<"ֻ"<<endl<<endl;
			}
		}
	}	
} 


//	8��
//	������Ľ� 
//	9��
