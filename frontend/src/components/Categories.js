import React from 'react';

const Categories = ({categories, showAndPostDashesAndInput, setCategory}) => {
    const handleClick = (category) => {
        setCategory(category);
        showAndPostDashesAndInput(category);
    };
    
    return (
        categories.map(item => {
            return (
                <button 
                    type="button" 
                    className="btn btn-outline-light"
                    key={item.id}
                    onClick={() => handleClick(item.category)}
                >
                    {item.category}
                </button>
            )
        })
    )
};

export default Categories