//ProbGEN function
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
int i;

double RuleProb ()
{
	for (i = 0; i < 1; i++)
	{
        if (High0 = 1)
        {
            Prob = 1.0;
            break;
        }

        else if (High1 = 1)
        {
            Prob = 0.75;
            break;
        }

        else if (High2 = 1)
        {
            Prob = 0.5;
            break;
        }

        else if (High3 = 1)
        {
            Prob = 0.25;
            break;
        }

        else if (High4 = 1)
        {
            Prob = 0.0;
            break;
        }

        else if (Med = 1)
        {
            Prob = 0.0;
            break;
        }

        else if (Low4 = 1)
        {
            Prob = 0.0;
            break;
        }

        else if (Low3 = 1)
        {
            Prob = 0.0;
            break;
        }

        else if (Low2 = 1)
        {
            Prob = 0.0;
            break;
        }

        else if (Low1 = 1)
        {
            Prob = 0.0;
            break;
        }

        else if (Low0 = 1)
        {
            Prob = 0.0;
            break;
        };

        return 0;
    }
} ;
//I would have used a switch statement if it werent for the fact that a switch only takes one argument


