# Saas-Django

I built a Software as a Service business by leveraging Django, Tailwind, htmx, Neon Postgres, Redis, and more.

## References

- Deploy Django on [Railway](https://kirr.co/qysgeu) with [this Dockerfile and guide](https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfile/)
- Create a One-Off Secret Key for Django [blog post](https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/)

## Getting Started

### Clone

```bash
mkdir -p ~/dev/saas
cd ~/dev/saas
git clone  https://github.com/oluoko/Saas-Django.git
```

### Create Virtual Environment

_macOS/Linux_

```bash
python3 --version # should be 3.11 or higher
python3 -m venv venv
source venv/bin/activate
```

_Windows_

```bash
c:\Python312\python.exe -m venv venv
.\venv\Scripts\activate
```

### Install Requirements

```bash
# with venv activated
pip install pip --upgrade && pip install -r requirements.txt
```

### Sample dotenv to dotnev

Follow the instructions in the `.env.example` file to create a `.env` file. You can use the following command to copy the example file:

```bash
cp .env.example .env
cat .env
```

### Create the _DJANGO_SECRET_KEY_

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

or

```bash
openssl rand -base64 64
```

or

```bash
python -c 'import secrets; print(secrets.token_urlsafe(64))'
```

Once you have this value, add update `DJANGO_SECRET_KEY` in `.env`.

### Create [Neon](https://kirr.co/eu0b31) Postgres Database

#### Install Neon CLI

Using the [Neon cli](https://neon.tech/docs/reference/cli-install) via [homebrew](https://brew.sh/):

```bash
brew install neonctl
```

#### Login to Neon CLI

```bash
neonctl auth
```

This will open a browser window to login.

#### Create a new Neon project (optional)

```bash
neonctl projects create --name saas
```
