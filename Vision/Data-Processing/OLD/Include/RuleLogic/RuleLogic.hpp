//RuleLogic function
#include <iostream>
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
bool myarray[11] = {High0, High1, High2, High3, High4, Med, Low4, Low3, Low2, Low1, Low0};

/*
	The rule logic function transforms the probability into a yes (1), maybe (0), and no (-1) state for later
	comparison with edge detection. If both edge and contrast function output yes then we are looking at target.
	If both output maybe then we are going to investigate further. If both output no then we are not looking at
	target. Here is the interesting part: if one of two states is yes and other is maybe then we are going to
	assume that we are looking at the target. If we get a no and a yes then we are also going to assume that
	we are NOT looking at the target. Let me repeat: yes and no output no.
*/

int RuleLogic (bool myarray)
{
    int x;
    if (Prob = 1.0)
    {
        x = 1;
        return x;
    }
    else if (Prob = 0.75)
    {
        x = 2;
        return x;
    }
    else if (Prob = 0.5)
    {
        x = 3;
        return x;
    }
    else if (Prob = 0.25)
    {
        x = 4;
        return x;
    }
    else if (Prob = 0.0)
    {
        x = 5;
        return x;
    };

	switch (x)
	{
		case 1:
			y = 1;
			break;
		case 2:
			y = 0;
			break;
		case 3:
			y = 0;
			break;
		case 4:
			y = -1;
			break;
		case 5:
			y = -1;
			break;
		default:
			cout << "ERROR, DEFAULT CASE ACTIVATED";
	};

	return (y);
};


