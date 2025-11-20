//random example (sorting String)
public class Example1
{
    public static String[] sortStrs(String[] toSort)
    {
        boolean sorted = false;
        while (!sorted) {
            for (int i = 0; i < toSort.length-1; i++) {
                if (toSort[i].compareTo(toSort[i+1])>0) {
                    String temp = toSort[i];
                    toSort[i] = toSort[i+1];
                    toSort[i+1] = temp;
                }
            }
            for (int i = 0; i < toSort.length-1; i++) {
                if (toSort[i].compareTo(toSort[i+1])>0)
                    break;
                if (i == toSort.length-2)
                    sorted = true;
            }
        }
        for (int i = 0; i < toSort.length-1; i++) {
            if (toSort[i]==toSort[i+1])
                toSort[i] = "";
        }
        return toSort 
    }
}