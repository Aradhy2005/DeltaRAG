# Authentication Guide

Users receive an authentication token after successful login.

The token should be included in every authenticated API request.

Clients should request a new token when the current token expires.

Authentication failures should return HTTP status 401.