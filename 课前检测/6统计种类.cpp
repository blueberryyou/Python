# include "iostream"
using namespace std;
int main(){
	char str[99];
	int s1=0,s2=0,s3=0,s4=0,s5=0;
	gets(str);//�����ո� 
	for(int i=0;str[i]!='\0';i++){ 	
		if(str[i]>=65&&str[i]<=90)
		s1++;
		else if(str[i]>=97&&str[i]<=122)
		s2++;
		else if(str[i]>=48&&str[i]<=57)
		s3++;
		else if(str[i]==32)
		s4++;
		else 
		s5++;
	}
	cout<<"��д��ĸ��"<<s1<<"��"<<endl;
	cout<<"Сд��ĸ��"<<s2<<"��"<<endl;
	cout<<"�����ַ���"<<s3<<"��"<<endl;
	cout<<"�ո���"<<s4<<"��"<<endl;
	cout<<"�����ַ���"<<s5<<"��"<<endl;
}

//	8��
//	�ַ�����Ӧ�� 
//	8��

