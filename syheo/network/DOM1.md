# Document Object Model

- DOM이란 무엇인가? 🆗
- Event Bubbling and Capturing
- Event delegation

# 한 문장 정리‼️

### DOM이란?

문서 객체 모델이며 HTML, XML 문서의 프로그래밍 Interface입니다. HTML코드의 엘리먼트에 대한 API를 제공합니다. 

---

# 0. DOM이란?

[MDN](https://developer.mozilla.org/ko/docs/Gecko_DOM_Reference/%EC%86%8C%EA%B0%9C) 에서 말하는 DOM의 정의

> 문서 객체 모델(The Document Object Model, DOM) 은 HTML, XML 문서의 **프로그래밍 interface**이다.

# 1. 그래서 DOM이 뭐냐. 맞춰봐

1. 내가 작성한 HTML 코드가 DOM이다
2. 페이지 View Source가 DOM이다
3. DevTools에서 보이는 코드가 DOM이다.

### 1. 내가 작성한 HTML 코드가 DOM이다

아님ㅋ 하지만 내가 작성한 코드가 브라우저에 의해 파싱되면 DOM이 됨.

### 2. 페이지 View Source가 DOM이다

아님ㅋ View Source는 그 페이지를 이루고 있는 HTML을 보여줄 뿐이며, 내가 작성한 HTML과 같음.

하지만 코드 작성시 백엔드 언어를 사용한 템플릿 파일을 이용한 경우, 정확히는 컴파일 된 결과를 말하는 것임. 혹은 작성된 코드에 대해 빌드 과정을 거친 다음에 웹사이트에 배포되는 경우엔 HTML 코드는 압축되거나 변형되었을 수도 있음.

### 3. DevTools에서 보이는 코드가 DOM이다.

정답~ 브라우저에서 지원하는 **개발자 툴에서 보이는 것이 바로 DOM**! 이 툴에서 시각적으로 표현한 DOM이 나의 HTML 코드와 동일할 수는 있지만, 대개는 달라지게 되며 DevTool에서는 이러한 변경 사항이 적용되어 표시됨.

# 2. DOM과 HTMl이 달라지는 경우

### 1. Case1: 브라우저가 HTML을 수정한 경우

내가 작성한 HTML에 실수가 있었고, 브라우저가 이를 대신 고친 경우

예를 들어, 테이블 엘리먼트 작성 시 필요 요건인 `<tbody>`를 빼먹고 `<table>`을 작성했다고 합시다. 브라우저는 `<tbody>`를 대신 자동으로 넣어 준 다음 DOM을 만듬.

- **자동 교정 Autocorrection**
    - 브라우저는 잘못된 HTML을 만나게 되면 자동으로 DOM을 생성하여 바로잡아 줌.
    - 가령, 가장 상단의 태그는 항상 `<html>`
    - .만약 이것이 작성한 HTML에선 존재하지 않더라도 브라우저에 의해 DOM에 항상 존재함.
    - `<body>` 역시 마찬가지
- 그 외에 브라우저가 주로 자동으로 고쳐주는 것들을 살펴보면.
    - HTML 파일에 "Hello"라는 단어 하나만 존재하더라도 브라우저는 이를 `html`과 `body` 으로 감싸고 `head`를 필수적으로 추가해 줌.
    - DOM을 생성하는 과정에서 태그의 닫는 짝이 없는 경우 자동 생성하여 맞춰서 오류를 수정해줌.
    - 자동 교정의 특이 케이스로, `<table>`은 항상 `<tbody>`를 가져야 하므로 `<tbody>`를 빠뜨렸을 경우 DOM이 생성될 때 자동으로 추가함.

### 2. Case2 : JavaScript로 DOM을 조작하는 경우

이런 HTML 코드를 작성했다고 가정.

```
<div id="container"></div>
```

그 후에 container에 텍스트를 추가하는 JavaScript를 작성했습니다.

```
<script>
  var container = document.getElementById("container");
  container.innerHTML = "New Content!";
</script>
```

DevTools에서 DOM을 체크하면 다음과 같이 바뀐 것을 알 수 있음.

그렇기 때문에 DevTools의 DOM은 원본 HTML 혹은 View Source와는 다른 것.

```
<div id="container">New Content!</div>
```

### 3. Case3 : Ajax and Templating

Ajax를 통해 어딘가에서 컨텐츠를 가져와서 현재 페이지에 넣거나, 클라이언트 사이드 템플리팅을 사용하는 경우에도 원래의 HTML과는 달라짐.

# 3. JavaScript & the DOM

- JavaScript : 브라우저가 읽고 **어떤 작업을 할 수 있는 언어.**
- DOM :  바로 이 작업이 이루어지는 **장소.**

사실 우리가 "JavaScript로 하는 것" 이라고 생각하는 것은.

- 정확히는 "DOM API" 이다!

**엘리먼트**에 `click` 이벤트가 일어나는지 감시하도록 JavaScript를 작성했다고 하자.

하지만 이 엘리먼트는 DOM 노드일 뿐,

우리는 DOM에 있는 DOM property를 통해서 listener를 붙여놓은 것임.

정리하자면, DOM은 브라우저에 의해 기록되는 모든 것임.

JavaScript는 이를 조작할 수 있는 문법이고 언어일 뿐이며, 이는 Node.js 등의 브라우저 밖의 DOM API가 없는 환경에서도 동작할 수 있음.

---

### 참고자료

[DOM이란 무엇인가?](https://velog.io/@godori/DOM%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)

[이벤트 버블링, 이벤트 캡처 그리고 이벤트 위임까지](https://joshua1988.github.io/web-development/javascript/event-propagation-delegation/)