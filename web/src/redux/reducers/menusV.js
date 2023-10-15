const menusV = (state = { isOpen: false }, action) => {

  switch(action.type) {

    case 'SWITCH_IS_OPEN':
      return {
        ...state,
        isOpen: !state.isOpen,
      }

    default: 
      return state;
  }
}

export default menusV;
