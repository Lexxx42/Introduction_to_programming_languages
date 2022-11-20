//повернуть слово
string word = "hello";
char[] newWord = new char[word.Length];


for (int i = 0; i < word.Length; i++)
{
    newWord[i]= word[word.Length-1-i];    
}

System.Console.WriteLine(newWord);
