# include "iostream"
using namespace std;
int main(){
	string str;
	cin>>str;
	for(int i=0;i<(str.length()/2);i++){
		if(str[i]!=str[str.length()-i-1]){
			cout<<"���ǻ�������";
			return 0;
		}
	cout<<"�ǻ�������";
	return 0;
	}
}

//	8��
//	�ַ�����Ӧ�� 
//	8��
