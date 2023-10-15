const mapsV = (state = { banks: [], route: undefined }, action) => {

  switch(action.type) {

    case 'CHANGE_BANKS':
      return {
        ...state,
        banks: action.value,
      }
    
    case 'SET_ROUTE':
      return {
        ...state,
        route: action.value,
      }

    default: 
      return state;
  }
}

export default mapsV;
