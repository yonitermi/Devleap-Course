#!/bin/bash
echo "Contents of /in:"
ls /in

echo "Contents of /out:"
ls /out

java -cp target/deps/pngtastic-1.0.jar -jar target/image-web-optimizer-0.0.2-SNAPSHOT.jar /in /out


