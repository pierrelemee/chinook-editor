FROM python:3.10-bullseye

# Files
RUN echo "alias ll='ls -l'" > /root/.bashrc
RUN echo "alias la='ls -la'" >> /root/.bashrc
RUN echo "alias runserver='pip install < requirements.txt && python manage.py runserver 0.0.0.0:8001'" >> /root/.bashrc
RUN echo "PS1='\[\033[01;35m\]\h \[\033[01;34m\]\w $\[\033[00m\] '" >> /root/.bashrc
RUN echo "export LANG='fr_FR.UTF8'" >> /root/.bashrc

WORKDIR /app

#CMD ["tail", "-f", "/dev/null"]
CMD ["sh", "-c", "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8001"]