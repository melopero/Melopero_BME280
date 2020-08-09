bme280.so: bme280.c bme280_pyhelper.c
	gcc -c -fpic bme280_pyhelper.c bme280.c
	gcc -shared -o bme280.so bme280.o bme280_pyhelper.o
	rm -v bme280.o bme280_pyhelper.o
clean:
	rm -v bme280.so
