import main,importlib
code=1
while code:
    code=main.main()
    importlib.invalidate_caches()
    importlib.reload(main)
