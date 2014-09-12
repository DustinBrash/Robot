//Probability to binary function
using namespace std;
double Prob;
bool High0;
bool High1;
bool High2;
bool High3;
bool High4;
bool Med;
bool Low4;
bool Low3;
bool Low2;
bool Low1;
bool Low0;
signed int y;
long myarray[11] = [High0, High1, High2, High3, High4, Med, Low4, Low3, Low2, Low1, Low0];

bool Prob2Bin (myarray)
{
	double x;
	if (x = 0.0)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 1;
	};

	if (x = 0.1)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 1;
		Low0 = 0;
	};

	if (x = 0.2)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 1;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.3)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 1;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.4)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 1;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.5)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 1;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.6)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 1;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.7)
	{
		High0 = 0;
		High1 = 0;
		High2 = 0;
		High3 = 1;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.8)
	{
		High0 = 0;
		High1 = 0;
		High2 = 1;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 0.9)
	{
		High0 = 0;
		High1 = 1;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	
	if (x = 1.0)
	{
		High0 = 1;
		High1 = 0;
		High2 = 0;
		High3 = 0;
		High4 = 0;
		Med = 0;
		Low4 = 0;
		Low3 = 0;
		Low2 = 0;
		Low1 = 0;
		Low0 = 0;
	};
	return (myarray);
};

