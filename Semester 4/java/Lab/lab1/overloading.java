class overloading{
    static int add(int a, int b)
    { 
        return a + b; 
    }
    static int add(int a, int b, int c)
    {
        return a + b + c;
    }
    public static void main(String args[])
    {
        System.out.println("add() with 2 parameters");
        System.out.println(add(2, 6));

        System.out.println("add() with 3 parameters");
        System.out.println(add(9, 3, 2));
    }
}