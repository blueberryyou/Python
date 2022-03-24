# include "iostream"
using namespace std;
int main(){
	char str[99];
	int s1=0,s2=0,s3=0,s4=0,s5=0;
	gets(str);//包含空格 
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
	cout<<"大写字母有"<<s1<<"个"<<endl;
	cout<<"小写字母有"<<s2<<"个"<<endl;
	cout<<"数字字符有"<<s3<<"个"<<endl;
	cout<<"空格有"<<s4<<"个"<<endl;
	cout<<"其他字符有"<<s5<<"个"<<endl;
}

//	8分
//	字符串的应用 
//	8分

