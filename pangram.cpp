#include<string>
#include<iostream>
using namespace std;
class Solution
{
public:
    bool checkIfPangram(string sentence)
    {
        bool found = true;
        if (sentence.length() < 26)
        {
            found = false;
            return found;
        }
        for (char i = 'A'; i <= 'Z'; i++)
            if (!(sentence.find(i)))
            {
                found = false;
                break;
            }
        return found;
    }
};
int main(int argc, char* argv[])
{
    Solution* solution = new Solution();
    cout << solution->checkIfPangram("jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo");
}

