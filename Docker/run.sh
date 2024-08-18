#############################################################
# AEYE Docker WEB Compose Starter
# Created By Yoonchul Chung
# Created At 2024.08.17
# Welcome to Visit Github : https://github.com/Yoonchulchung
#############################################################


initiate_docker_compose()
{
  clear
  figlet WELOCME TO 
  figlet AEYE WEB
  cd .. && cd .. && cd Docker && docker-compose up 2>&1 | tee docker-compose.log
}

npm_install()
{
  apt install npm
  cd ../AEYE_Front/AEYE_Front/ && npm install
}

run()
{
  npm_install

  initiate_docker_compose
}

run