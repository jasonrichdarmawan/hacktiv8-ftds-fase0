'use strict';

const e = React.createElement;

function LikeButton() {
  const [liked, setLiked] = useState(0);

  return (
    <button onClick={() => setLiked(true)}>
        Click me
    </button>
  )
}

// class LikeButton extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = { liked: false };
//   }

//   render() {
//     if (this.state.liked) {
//       return 'You liked this.';
//     }

//     return e(
//       'button',
//       { onClick: () => this.setState({ liked: true }) },
//       'Like'
//     );
//   }
// }

const domContainer = document.querySelector('#like_button_container');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));