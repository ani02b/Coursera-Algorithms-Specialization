public class Try
{
    public static void main(String[] args) {
        int x=-2147483648;
        double n=Math.abs(x);
        System.out.println(n);
        if(Math.abs(x)>=(int)Math.pow(2, 31))
        System.out.println(0);
    }
}