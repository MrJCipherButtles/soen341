Required:
- MySQL
- Python 3.6+

Steps:
1. Execute `library.sql` on fresh MySQL server
2. Execute `inserts.sql` on that same server
3. In root folder, run `pip install -r requirements.txt`
4. Run `python library.py`
5. Navigate to `localhost:5000`

When making changes, stop the server with `Ctrl+C`. Restart it by
running `python library.py` again