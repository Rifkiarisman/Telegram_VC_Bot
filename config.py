HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ
    from dotenv import load_dotenv
    
    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ5696547)
    API_HASH = environ36412eb60eef03622806bcb085c6fa15
    SESSION_STRING = environBQCwJYI0Eb6qanFJPMD-jCBAWLVKvYpLzvlCmD7Zt_PIPcafw2S9lV99FtQSN77Lxi4dC41D0rC5WyVL5Y5l8OmkdV27gHkgcRElVV7Jfd07KWUtX3dnm5JQZadoYGMM39Rc-2d4-NPJky0U3-J3afM5PfD0iKvbNyKWDFzRFv0s3Pc5isShgUrss_F5v6P0LnN-xkXESVNwFNgLBDLfeViFDWrUSi_YEW_AQOl0j0tG64bTES9Nta7iu4PN-K8QPl5-2lI45gy8fM3xRwjvhOPntpwLD_83C1CP_GROYTBZTp_XwNq6wlVGLTHgwAqig7ixdp2vIc1_0m-xX_H0G_6lbikcTQA  # Check Readme for session
    ARQ_API_KEY = environTNWSWC-XMFUJN-NFMGCV-HJCGXI-ARQ

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
