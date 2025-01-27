1. Należy pobrać obraz:

docker pull thatpalal/price_predictor

2. Uruchomienie kontenera;
docker run -p 8080:8080 thatpalal/price_predictor

3. Aplikacja powinna działać pod adresem:
http://127.0.0.1:8080 - chyba, że port został manualnie zmieniony, w przypadku zajętego 8080.

4. Gotowe do przetestowania:
curl -X POST http://127.0.0.1:8080/predict -H "Content-Type: application/json" -d '{"area": X, "rooms": Y}' - trzeba zastąpić wartości X i Y liczbami, które nas interesują.





