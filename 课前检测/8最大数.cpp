# include "iostream"
using namespace std;
int main(){
	int a[10];
	for(int i=0;i<10;i++)
	cin>>a[i];
	int max=a[0],k=0;
	for(int i=1;i<10;i++){
		if(a[i]>max){
			max=a[i];
			k=i;
		}
	}
	cout<<"�����"<<max<<"λ�ã�"<<k+1;
} 

//	8��
//	�ȴ�С
//	8��
