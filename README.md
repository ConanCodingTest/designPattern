# Incorporating design patterns into software development.

## design Pattern

1.  Observer Pattern
    - 對一個物件狀態或資料的更新需要其他物件同步更新
    - 物件僅需要將自己的更新通知給其他物件，而不需要知道其細節
    - 應用：帳號異常登錄檢測
2.  State Pattern
    - 物件的行為取決於狀態，且運行時經常改變狀態
    - 操作中含有大量分支的條件陳述式，且分支依賴物件的狀態
    - 應用：自動化流程控制
3.  Mediator Pattern
    - 一組物件以定義良好但複查方式進行通訊
    - 一個物件引用其他很多物件且直接與其通訊
    - 想透過中間類來封裝多個類別行為
    - 應用：通訊軟體的通訊裝置連線
4.  Decorator Pattern
    - 大量獨立擴展，為支援每一種組合將產生大量子類別
    - 需要動態增加或撤銷功能
    - 無法採用生成子類別的方式進行擴充
    - 應用：過濾程式
5.  Singleton Pattern
    - 類別只允許一個實例
    - 應用：全域管理類別
6.  Clone Pattern
    - 通常使用 deepcopy
    - 創造新物件很複雜
    - 類別的初始化需要消耗很多資源
    - 應用：配合備忘錄模式做備份工作
7.  Chain of Responsibility Pattern
    - 多個物件可以處理同一個請求
    - 請求處理具有明顯一層一層傳遞關係
    - 請求的流程和順序需要程式運行時動態確定
    - 應用：簽呈系統
8.  Proxy Pattern
    - 不能直接引用物件時
    - 對一個物件功能進行加強時
    - 應用：遠端代理、防火牆代理
9.  Facade Pattern
    - 需要為一個複雜的子系統提供簡單介面時
    - 客戶程式與多個子系統之間存在很大的依賴關係
10. Iterator Pattern
    - 集合的內部結構複雜，不想暴露細節
    - 需要統一的存取介面，對不同的集合使用統一的演算法
11. Composite Pattern
    - 物件之間具有明顯的"部分-整體"關係 or 層次關係
    - 組合物件與單獨物件具有相同或類似的行為
12. Builder Pattern
    - 產品創建過程複雜，需要將創建過程與功能分開
    - 不同的創建順序或不同的組合方式，將創建不同產品
13. Adapter Pattern
    - 系統需要使用現有的類別
    - 應用：己方系統拓展新功能
14. Strategy Pattern
    - 系統需要動態的在幾種演算法中選一種
    - 設計程式介面時，希望部分內部實現由呼叫方自行實現
15. Factory Pattern
    - 系統中有多於一個的產品族，且每次只使用其中某一產品族
    - 產品結構穩定，不會變動產品結構
16. Command Pattern
    - 系統發送命令，任務馬上得到處理
    - 一系列命令組合一起操作
    - 應用：聚集命令
17. Memento Pattern
    - 需要保存/恢復物件的狀態或資料
    - 需要實現撤銷/恢復功能
    - 需要可回滾的操作
    - 資料庫的事務管理
18. Flyweight Pattern
    - 系統大量相同物件被使用，造成記憶體大量損耗
    - 物件的大部分狀態可以外部化，將外部化狀態傳入物件
    - 應用：瀏覽器的緩存
19. Visitor Pattern
    - 物件結構中包含物件類別型比較少，且類別需求固定，但經常需要在物件結構上定義新操作
    - 物件結構包含多個類別型的物件，希望這些物件實施一些依賴其具體類別型的操作
20. Template Pattern
    - 一次實現一個演算法不變的部分，可變的行為留給子類別
21. Bridge Pattern
    - 一個產品有多種分類及組合
22. Interpreter Pattern
23. Filter Pattern
    - 需要對物件清單進行檢驗
    - 應用：敏感詞過濾、網路介面的請求即回應進行攔截
24. Object pool Pattern
    - 初始化及銷毀的代價很高，且需要經常被產生實體的物件
    - 應用：資料庫連接池、執行緒池
25. Callback Pattern
    - 非同步執行
    - 應用：讀檔、發送 Http 請求
26. MVC Pattern
    - 應用：互聯網網頁前後端分離

## SOLID Principle

- Single Responsibility Principle
- Open Close Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependence Inversion Principle

## Code refactoring

1. Rename(variable、function、class)
2. function refactoring
3. data structure refactoring
4. use design pattern
