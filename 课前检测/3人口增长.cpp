# include "iostream"
using namespace std;
int main(){
	double x,i;
	x=12.9533;
	for(int i=1;;i++){
		x=x*(1+0.0107); 
		if(x>=15){
			cout<<i<<"����ҹ��˿ڴﵽ�򳬹�15�ڡ�"; 
			return 0; 
		} 
	}
}

//	9��
//	�۳˵�����
//10fen 
