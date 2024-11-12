#include <stdio.h>

int main() {
    int numero1; 
    int numero2;
    int prodotto;

    printf("\nInserisci primo numero: ");
    scanf("%d", &numero1);

    printf("\nInserisci secondo numero: ");
    scanf("%d", &numero2);
    
    prodotto = numero1 * numero2;
    
    printf("\nIl prodotto è:");
    printf("\n%d * %d = %d\n", numero1, numero2, numero1 * numero2);

    return 0;

}