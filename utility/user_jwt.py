from datetime import datetime, timezone
import jwt
import datetime
import time
from flask import request, jsonify

access_secret = "secret"
refresh_secret = "refresh"

def get_access_token(user_id, ban_list = []):
    if user_id in ban_list:
        raise Exception("user is banned")

    expiry = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=15)
    return jwt.encode({"exp": expiry, "sub": user_id, "iss": "LASSES APP"}, access_secret, algorithm="HS256")

def decode_access_token(access_token):
    return jwt.decode(access_token, access_secret, algorithms=["HS256"])

def get_refresh_token(user_id):
    expiry = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=30)
    return jwt.encode({"exp": expiry, "sub": user_id, "iss": "LASSES APP"}, refresh_secret, algorithm="HS256")

def decode_refresh_token(refresh_token):
    return jwt.decode(refresh_token, refresh_secret, algorithms=["HS256"])

def get_access_token_from_refresh_token(refresh_token, ban_list = []):
    try:
        decoded = decode_refresh_token(refresh_token)
    except: 
        raise Exception("refresh token has expired")

    return get_access_token(decoded.get('sub'), ban_list)

# def check_auth():    
#     if not request.headers.has_key('Authorization'):
#         return jsonify({"error": "You are not authorized"})

#     bearer = request.headers.get('Authorization')
#     token = bearer[len("Bearer "):]

#     try:
#         decoded = decode_access_token(token)
#         return decoded
#     except:
#         return jsonify({"error": "You are not authorized"})
