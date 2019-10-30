# image-processing

| HTTP Method | Action | Example |
|---|---|---|
|POST|Convert to black and white an image| http://localhost:5000/image-processing/bw|
|GET|Retrieve list of images|http://localhost:5000/image-processing/images|
|   |   |   |

```
curl -i -H "Content-Type: application/json" -X POST -d '{"path": "../image-storage/img03.jpg"}' http://localhost:5000/image-processing/bw
curl -i http://localhost:5000/image-processing/images
```
