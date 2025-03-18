def longest_bitonic_subarray(arr):
    n = len(arr)  # Longitud del arreglo

    # Paso 1: Construir el arreglo inc[] (longitudes crecientes)
    # inc[i] almacena cuánto ha crecido la secuencia hasta el índice i
    inc = [1] * n  # Inicializamos todo con 1 porque cada número por sí solo es una secuencia
    for i in range(1, n):  # Recorremos desde el segundo elemento
        if arr[i] > arr[i - 1]:  # Si el actual es mayor que el anterior, sigue creciendo
            inc[i] = inc[i - 1] + 1  # Se suma 1 a la longitud creciente anterior

    # Paso 2: Construir el arreglo dec[] (longitudes decrecientes)
    # dec[i] almacena cuánto ha decrecido la secuencia desde el índice i
    dec = [1] * n  # Igual que inc[], cada número solo cuenta como una secuencia
    for i in range(n - 2, -1, -1):  # Recorremos desde el penúltimo elemento hacia atrás
        if arr[i] > arr[i + 1]:  # Si el actual es mayor que el siguiente, sigue decreciendo
            dec[i] = dec[i + 1] + 1  # Se suma 1 a la longitud decreciente siguiente

    # Paso 3: Encontrar el máximo de (inc[i] + dec[i] - 1)
    # max_length almacena la longitud máxima de una subsecuencia bitónica
    max_length = 0
    peak_index = 0  # Aquí guardaremos el índice del pico (máximo)

    for i in range(n):  # Recorremos todo el arreglo
        bitonic_length = inc[i] + dec[i] - 1  # Fórmula: subida + bajada - 1 (para no contar dos veces el pico)
        if bitonic_length > max_length:  # Si encontramos una montaña más larga
            max_length = bitonic_length  # Guardamos la nueva longitud máxima
            peak_index = i  # Guardamos el índice del pico (máximo)

    # Paso 4: Extraer la subsecuencia bitónica más larga
    start = peak_index - (inc[peak_index] - 1)  # Índice de inicio de la secuencia
    end = peak_index + (dec[peak_index] - 1)  # Índice de fin de la secuencia
    bitonic_subarray = arr[start:end + 1]  # Extraemos la subsecuencia bitónica

    return bitonic_subarray  # Devolvemos la subsecuencia más larga

# Ejemplo de uso
arr = [1, 2, 5, 3, 2, 1, 4, 6, 3, 2]
print(longest_bitonic_subarray(arr))  # Salida: [1, 2, 5, 3, 2, 1]
