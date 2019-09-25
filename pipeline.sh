#!/bin/zsh

##nginx change
# docker build -t lunacircle4/nginx:floweryroad-backend -f \
# /Users/kimdongwon/Documents/WebProgramming/Projects/Floweryroad/floweryroad-backend/nginx/prod/Dockerfile \
# /Users/kimdongwon/Documents/WebProgramming/Projects/Floweryroad/floweryroad-backend/nginx
# docker push lunacircle4/nginx:floweryroad-backend

docker build -t lunacircle4/floweryroad-backend:1.3.2  -f  \
/Users/kimdongwon/Documents/WebProgramming/Projects/Floweryroad/floweryroad-backend/web/docker/prod/Dockerfile \
/Users/kimdongwon/Documents/WebProgramming/Projects/Floweryroad/floweryroad-backend/web
docker push lunacircle4/floweryroad-backend:1.3.2

docker tag lunacircle4/floweryroad-backend:1.3.2 lunacircle4/floweryroad-backend:latest
docker push lunacircle4/floweryroad-backend:latest

scp -i /Users/kimdongwon/Documents/WebProgramming/credential/floweryroad.pem -r \
/Users/kimdongwon/Documents/WebProgramming/Projects/Floweryroad/floweryroad-backend/.credential/prod/* \
ec2-user@15.164.30.120:/app/.credential/

scp -i /Users/kimdongwon/Documents/WebProgramming/credential/floweryroad.pem \
/Users/kimdongwon/Documents/WebProgramming/Projects/Floweryroad/floweryroad-backend/docker-compose/prod/docker-compose.yml \
ec2-user@15.164.30.120:/app/

ssh -tt -i /Users/kimdongwon/Documents/WebProgramming/credential/floweryroad.pem ec2-user@15.164.30.120   "\
                                    docker-compose -f /app/docker-compose.yml stop  && \
                                    docker-compose -f /app/docker-compose.yml pull  && \
                                    docker-compose -f /app/docker-compose.yml up -d"