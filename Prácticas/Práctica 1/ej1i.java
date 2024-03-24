import java.util.ArrayList;

public class ej1i {
    public static void main(String[] args) {
        int[] c = {6, 12, 6};
        int i = c.length;
        int k = 0;
        int r = 0;
        for (int e : c) {
            r += e;
        }
        ArrayList<Integer> solucion = new ArrayList<>();
        ArrayList<Integer> parcial = new ArrayList<>();
        System.out.println(subsetSum(c, i, k, r, parcial, solucion));
        System.out.println("Elementos del ArrayList:");
        System.out.println(solucion.isEmpty()); //devuelve vacio - problema con la referencia??
        for (int elemento : solucion) {
            System.out.println(elemento);
        }

    }

    public static boolean subsetSum(int[] c, int i, int k, int r, ArrayList<Integer> parcial, ArrayList<Integer> solucion) {
        if (k < 0) {
            return false;
        }
        if (k > r) {
            return false;
        }
        if (i == 0) {
            if (k == 0) {
                solucion = new ArrayList<>(parcial); // Crear una nueva instancia de ArrayList y copiar elementos
                return true;
            } else {
                return false;
            }
        }
        r -= c[i - 1];
        if (subsetSum(c, i - 1, k, r, parcial, solucion)) {
            return true;
        }
        parcial.add(c[i - 1]);
        if (subsetSum(c, i - 1, k - c[i - 1], r, parcial, solucion)) {
            return true;
        }
        parcial.remove(Integer.valueOf(c[i - 1]));
        return false;
    }
}
