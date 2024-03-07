1. Modbus
執行
`pip install -r requirements.txt`
修改./main.py中ModbusTcpClient的相關資訊後執行
`python3 ./main.py`
Note: 由於function採用非同步方式設計，因此顯示資料時不會等待全部的子任務fetch完資料再一併顯示資料
2. ZPL
請參照label.zpl