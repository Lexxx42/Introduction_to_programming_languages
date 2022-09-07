




string text = "sdfsd iaeurh oawei IOOHDFQAw oqPWH"
+"ASDFASE we f3245 2as df asd";

// string s = "qwerty"
//             012345

string Replace(string text, char oldValue, char newValue)
{
    string result = String.Empty;
    int length = text.Length;
    for (int i = 0; i < length; i++)
    {
        if(text[i]==oldValue) result = result+ $"{newValue}";
        else result = result + $"{text[i]}";
    }
    return result;
}

string newText = Replace(text, ' ', '|');
System.Console.WriteLine(newText);
System.Console.WriteLine();
newText = Replace(newText, 'k', 'K');