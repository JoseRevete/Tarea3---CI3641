#include <stdio.h>
#include <time.h>
#include <errno.h>
#include <stdlib.h>

// Recorrer la matriz por fila y columna. Dinamico
void recorrerFilaColumna(int **matriz, int N, int M) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            matriz[i][j];
        }
    }
}

// Recorrer la matriz por columna y fila. Dinamico
void recorrerColumnaFila(int **matriz, int N, int M) {
    int i, j;
    for (j = 0; j < M; j++) {
        for (i = 0; i < N; i++) {
            matriz[i][j];
        }
    }
}

// Recorrer la matriz por fila y columna. Estatico
void recorrerFilaColumnaEstatica(int matriz[][1000], int K, int L) {
    int i, j;
    for (i = 0; i < K; i++) {
        for (j = 0; j < L; j++) {
            matriz[i][j];
        }
    }
}

// Recorrer la matriz por columna y fila. Estatico
void recorrerColumnaFilaEstatica(int matriz[][1000], int K, int L) {
    int i, j;
    for (j = 0; j < L; j++) {
        for (i = 0; i < K; i++) {
            matriz[i][j];
        }
    }
}

// Función principal
int main(void) {
    int arreglo[] = {100, 1000, 10000, 100000, 1000000};
    int arreglo2[] = {100, 1000, 10000};
    int k = 0;
    float arregloTiempos1[25] = {0};
    float arregloTiempos2[25] = {0};
    float arregloTiempos3[16] = {0};
    float arregloTiempos4[16] = {0};

    // Crear archivo de resultados
    FILE *fp = fopen("resultados.csv", "w");
    if (fp == NULL) {
        perror("Error al abrir el archivo");
        return EXIT_FAILURE;
    }
    fprintf(fp, "N,M,TiempoFilaColumna,TiempoColumnaFila\n");

    // Crear archivo de resultados estaticos
    FILE *fp2 = fopen("resultadosEstaticos.csv", "w");
    if (fp2 == NULL) {
        perror("Error al abrir el archivo");
        return EXIT_FAILURE;
    }
    fprintf(fp2, "K,L,TiempoFilaColumna,TiempoColumnaFila\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            int N = arreglo[i];
            int M = arreglo[j];
            
            printf("--------------------\n");
            printf("Matriz de %d x %d\n", N, M);

            // Crear matriz dinamica
            int **matriz = (int **)malloc(N * sizeof(int *));
            for (int k = 0; k < N; k++) {
                matriz[k] = (int *)malloc(M * sizeof(int));
            }

            float promedio1 = 0;
            float promedio2 = 0;

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

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            int K = arreglo2[i];
            int L = arreglo2[j];

            // Crear matriz estatica
            int matrizEstatica[1000][1000] = {0};

            float promedio3 = 0;
            float promedio4 = 0;

            for (int k = 0; k < 3; k++) {
                clock_t timeStart = clock();
                recorrerFilaColumnaEstatica(matrizEstatica, K, L);
                clock_t timeEnd = clock();
                float seconds2 = (float)(timeEnd - timeStart) / CLOCKS_PER_SEC;
                promedio3 += seconds2;

                timeStart = clock();
                recorrerColumnaFilaEstatica(matrizEstatica, K, L);
                timeEnd = clock();
                seconds2 = (float)(timeEnd - timeStart) / CLOCKS_PER_SEC;
                promedio4 += seconds2;
            }

            promedio3 /= 3;
            promedio4 /= 3;
            arregloTiempos3[k] = promedio3;
            arregloTiempos4[k] = promedio4;

            fprintf(fp2, "%d,%d,%f,%f\n", K, L, promedio3, promedio4);
        }
    }

    fclose(fp);
    fclose(fp2);
    return 0;
}