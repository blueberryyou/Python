# include "iostream"                            //����81 
using namespace std;                            //����85
int main(){                            			//���ؽ� 
	int a[10],t;
	for(int i=0;i<10;i++)
	cin>>a[i];
	for(int i=9;i>-0;i--){
		for(int j=0;j<i;j++){
			if(a[j]<a[j+1]){
				t=a[j+1];
				a[j+1]=a[j];
				a[j]=t;
			}
		}
	}
	for(int i=0;i<10;i++)
	cout<<a[i]<<"\t";
}

//	8��
//	���� 
//	8��
