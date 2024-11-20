#include <stdio.h>
#include <time.h>
#include <errno.h>
#include <stdlib.h>

// Recorrer la matriz por fila y columna
void recorrerFilaColumna(int **matriz, int N, int M) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            matriz[i][j];
        }
    }
}

// Recorrer la matriz por columna y fila
void recorrerColumnaFila(int **matriz, int N, int M) {
    int i, j;
    for (j = 0; j < M; j++) {
        for (i = 0; i < N; i++) {
            matriz[i][j];
        }
    }
}

// Función principal
int main(void) {
    int arreglo[] = {100, 1000, 10000, 100000, 1000000};
    int k = 0;
    float arregloTiempos1[25] = {0};
    float arregloTiempos2[25] = {0};
    float promedio1 = 0;
    float promedio2 = 0;

    // Crear archivo de resultados
    FILE *fp = fopen("resultados.csv", "w");
    if (fp == NULL) {
        perror("Error al abrir el archivo");
        return EXIT_FAILURE;
    }
    fprintf(fp, "N,M,TiempoFilaColumna,TiempoColumnaFila\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            int N = arreglo[i];
            int M = arreglo[j];
            printf("--------------------\n");
            printf("Matriz de %d x %d\n", N, M);

            int **matriz = (int **)malloc(N * sizeof(int *));
            for (int k = 0; k < N; k++) {
                matriz[k] = (int *)malloc(M * sizeof(int));
            }

            for (int k = 0; k < 3; k++) {
                clock_t timeStart = clock();
                recorrerFilaColumna(matriz, N, M);
                clock_t timeEnd = clock();
                float seconds = (float)(timeEnd - timeStart) / CLOCKS_PER_SEC;
                promedio1 += seconds;
                printf("Tiempo de recorrerFilaColumna: %f segs\n", seconds);

                timeStart = clock();
                recorrerColumnaFila(matriz, N, M);
                timeEnd = clock();
                seconds = (float)(timeEnd - timeStart) / CLOCKS_PER_SEC;
                promedio2 += seconds;
                printf("Tiempo de recorrerColumnaFila: %f segs\n", seconds);
            }
            promedio1 /= 3;
            promedio2 /= 3;
            arregloTiempos1[k] = promedio1;
            arregloTiempos2[k] = promedio2;

            fprintf(fp, "%d,%d,%f,%f\n", N, M, promedio1, promedio2);

            for (int k = 0; k < N; k++) {
                free(matriz[k]);
            }
            free(matriz);
            k++;
        }
    }

    fclose(fp);
    return 0;
}