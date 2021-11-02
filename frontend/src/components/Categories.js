import React from 'react';

const Categories = ({categories}) => {
    return (
        categories.map(item => {
            return (
                <button 
                    type="button" 
                    className="btn btn-outline-light"
                    key={item.id}
                >
                    {item.category}
                </button>
            )
        })
    )
};

export default Categories