
string text = "Тестирование продукта→обнаружение ошибок→анализ ошибок";

// string s = "qwerty"
//             012345

string Replace(string text, char oldValue, char newValue)
{
    string result = String.Empty;
    int length = text.Length;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == oldValue) result = result + $"{newValue}";
        else result = result + $"{text[i]}";
    }
    return result;
}

string newText = Replace(text, '→', '>');
System.Console.WriteLine(newText);
