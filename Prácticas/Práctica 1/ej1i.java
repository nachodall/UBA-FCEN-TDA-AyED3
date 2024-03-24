import java.util.Vector;

public class ej1i {
    public static void main(String[] args) {
        int[] c = {6,12,6};
        int i = 0;
        int k = 0;
        Vector<Integer> parcial = new Vector<>();
        subsetSum(c, i, k, parcial);
       
    }
    public static Vector<Integer> eliminarElemento(Vector<Integer> vector, int elemento) {
        Vector<Integer> nuevoVector = new Vector<>();
        
        for (int i = 0; i < vector.size(); i++) {
            if (vector.get(i) != elemento) {
                nuevoVector.add(vector.get(i));
            }
        }
        
        return nuevoVector;
    }

    public static Vector<Integer> subsetSum(int[] c, int i, int k, Vector<Integer> parcial){
        if (k<0){
            return new Vector<Integer>();
        }

        if (i==0){
            if (k==0){
                return parcial;
            } else {
                return new Vector<Integer>();
            }
        }

        parcial.add(c[i]);
        return subsetSum(c, i-1, k, parcial);
        eliminarElemento(parcial, c[i]);
        return subsetSum(c, i-1, k-c[i], parcial);
    }

}

