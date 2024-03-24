public class ej1{
    public static void main(String[] args) {
        int[] c = {6, 12, 6};
        int i = c.length;
        int k = 12;
        boolean res = subsetSum(c,i,k);
        System.out.println(res);
    }

    public static boolean subsetSum(int[] c, int i, int k){
        if (k<0){ //regla de factabilidad del ejercicio
            return false;
        }

        if (i==0){
            return (k==0);
        }

        if (c[i-1] > k){ //ignorar proximos elementos si el actual es mayor a k, digo i-1 xq el index arranca en 0
            return subsetSum(c, i-1, k); 
        }

        return subsetSum(c, i-1, k) || subsetSum(c, i-1, k-c[i]);
    }
}